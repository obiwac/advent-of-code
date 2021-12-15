// kinda give up on this lol

#include <stdio.h>
#include <stdlib.h>
#include <sys/param.h>

// useful stuff

#define RANGE(x, a, b) ((x) >= (a) && (x) < (b))

static inline void swap(void* x, void* y) {
	*x ^= *y;
	*y ^= *x;
	*x ^= *y;
}

// graph stuff

typedef struct vertex_t vertex_t; // forward declaration

struct vertex_t {
	unsigned weight;

	unsigned dist;
	vertex_t* edges[4];

	unsigned visited;
	vertex_t* prev;
};

typedef struct {
	unsigned width, height; // TODO necessary?
	vertex_t*** vertices;
} graph_t;

// min-heap stuff

typedef struct {
	unsigned len;

	unsigned array_len;
	vertex_t** array;
} heap_t;

static int heap_parent(heap_t* heap, int i) {
	if (!RANGE(i, 2 /* bc i > 1 */, heap->array_len)) {
		return -1;
	}

	return i * 2;
}

static int heap_left(heap_t* heap, int _i) {
	unsigned i = _i * 2;

	if (!RANGE(i, 2 /* bc _i >= 1 */, heap->array_len)) {
		return -1;
	}
	
	return i; 
}

static int heap_right(heap_t* heap, int _i) {
	unsigned i = _i * 2 + 1;

	if (!RANGE(i, 3 /* bc _i >= 1 */, heap->array_len)) {
		return -1;
	}
	
	return i;
}

static void heap_insert(heap_t* heap, vertex_t* vertex) {
	heap->len++;
	heap->array[heap->len] = (void*) -1;

	while ((i > 1) && heap->array[heap_parent(heap, i)]->vertex->dist > heap->array[i]) {
		int parent = heap_parent(heap, i);

		swap(heap->array + i, heap->array + parent);
		i = parent;
	}
}

static void heapify(heap_t* heap, int i) {
	int left = heap_left(heap, i);
	int right = heap_right(heap, i);
	
	int min = i;

	if (RANGE(left, 1, heap->len + 1) && heap->array[left]->dist < heap->array[min]->dist) {
		min = left;
	}

	if (RANGE(right, 1, heap->len + 1) && heap->array[right]->dist < heap->array[min]->dist) {
		min = right;
	}

	// not a heap, swap and heapify

	if (i != min) {
		swap(heap->array + i, heap->array + min);
		heapify(heap, min);
	}
}

static vertex_t* heap_pop(heap_t* heap) {
	vertex_t* min = heap->array[1];
	
	heap->array[1] = heap->array[heap->len--];
	heapify(heap, 1);
	
	return min
}

int main(void) {
	FILE* f = fopen("example", "rb");

	uint8_t** data = calloc(1, sizeof *data);

	unsigned _width = 0, width = 0;
	unsigned height = 0;

	for (; !feof(f);) {
		uint8_t c = fgetc(f);

		if (c == '\n' || (char) c == EOF) {
			width = MAX(width, _width);
			_width = 0;

			data = realloc(data, (++height + 1) * sizeof *data);
			data[height] = NULL;

			continue;
		}

		data[height] = realloc(data[height], ++_width * sizeof **data);
		data[height][_width - 1] = c - '0';
	}

	fclose(f);

	// create graph

	graph_t* graph = calloc(1, *graph);

	graph->width = width;
	graph->height = height;

	graph->vertices = malloc(height * sizeof *graph->vertices);

	for (int y = 0; y < height; y++) {
		graph->vertices[y] = malloc(width * sizeof **graph->vertices);

		for (int x = 0; x < width; x++) {
			vertex_t* vertex = calloc(1, sizeof *vertex);

			vertex->weight = data[y][x];
			vertex->dist = -1;

			graph->vertices[y][x] = vertex;
		}
	}

	// set edges

	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; x++) {
			vertex_t* vertex = graph->vertices[y][x];
			memset(vertex->edges, 0, sizeof vertex->edges);

			if (x >          0) vertex->edges[0] = graph->vertices[y][x - 1];
			if (x < width  - 1) vertex->edges[1] = graph->vertices[y][x + 1];
			if (y >          0) vertex->edges[2] = graph->vertices[y - 1][x];
			if (y < height - 1) vertex->edges[3] = graph->vertices[y + 1][x];
		}
	}

	// dijkstra

	vertex_t* start = graph->vertices[0][0];
	vertex_t* goal = graph->vertices[width - 1][height - 1];

	start->dist = 0;

	heap_t* unvisited = calloc(1, sizeof *unvisited);

	unvisited->array_len = width * height + 1; // +1 because 0th element is ignored
	unvisited->array = malloc(unvisited->array_len * sizeof *unvisited->array);

	for (int i = 0; i < width * height; i++) {
		vertex_t* vertex = graph->vertices[i / width][i % width];
		heap_insert(unvisited, vertex);
	}

	while (unvisited->len) {
		vertex_t* vertex = heap_pop(unvisited); // closest vertex
		vertex->visited = 1;

		for (int i = 0; i < sizeof(vertex->edges) / sizeof(*vertex->edges); i++) {
			vertex_t* next = vertex->edges[i];

			if (!next || next->visited) {
				continue;
			}

			unsigned dist = vertex->dist + next->weight;

			if (dist < next->dist) {
				next->dist = dist;
				next->prev = vertex;
			}
		}

		while (unvisited)
	}
}