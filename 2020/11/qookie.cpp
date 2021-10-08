#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>

// ------------------------ Part 1 ----------------------------

bool occupied_at(const std::vector<std::string> &lines, int x, int y) {
	if (y < 0 || y >= lines.size())
		return false;

	if (x < 0 || x >= lines[y].size())
		return false;

	return lines[y][x] == '#';
}

int count_neighbors_p1(const std::vector<std::string> &lines, int x, int y) {
	int n = 0;
	if (occupied_at(lines, x - 1, y - 1)) n++;
	if (occupied_at(lines, x,     y - 1)) n++;
	if (occupied_at(lines, x + 1, y - 1)) n++;
	if (occupied_at(lines, x - 1, y    )) n++;
	if (occupied_at(lines, x + 1, y    )) n++;
	if (occupied_at(lines, x - 1, y + 1)) n++;
	if (occupied_at(lines, x,     y + 1)) n++;
	if (occupied_at(lines, x + 1, y + 1)) n++;

	return n;
}

std::vector<std::string> run_iter_p1(const std::vector<std::string> &lines) {
	std::vector<std::string> out = lines;

	for (int y = 0; y < lines.size(); y++) {
		auto line = lines[y];

		for (int x = 0; x < line.size(); x++) {
			char c = line[x];

			int occ_neigh = count_neighbors_p1(lines, x, y);

			if (c == 'L' && occ_neigh == 0) {
				c = '#';
			} else if (c == '#' && occ_neigh >= 4) {
				c = 'L';
			}

			out[y][x] = c;
		}
	}

	return out;
}

// ------------------------ Part 2 ----------------------------

bool any_on_line(const std::vector<std::string> &lines, int x, int y, int dx, int dy) {
	x += dx;
	y += dy;

	while (y >= 0 && y < lines.size() && x >= 0 && x < lines[y].size()) {
		if (lines[y][x] == 'L')
			return false;
		if (lines[y][x] == '#')
			return true;

		x += dx;
		y += dy;
	}

	return false;
}

int count_neighbors_p2(const std::vector<std::string> &lines, int x, int y) {
	int n = 0;
	if (any_on_line(lines, x, y, -1, -1)) n++;
	if (any_on_line(lines, x, y,  0, -1)) n++;
	if (any_on_line(lines, x, y,  1, -1)) n++;
	if (any_on_line(lines, x, y, -1,  0)) n++;
	if (any_on_line(lines, x, y,  1,  0)) n++;
	if (any_on_line(lines, x, y, -1,  1)) n++;
	if (any_on_line(lines, x, y,  0,  1)) n++;
	if (any_on_line(lines, x, y,  1,  1)) n++;

	return n;
}

std::vector<std::string> run_iter_p2(const std::vector<std::string> &lines) {
	std::vector<std::string> out = lines;

	for (int y = 0; y < lines.size(); y++) {
		auto line = lines[y];

		for (int x = 0; x < line.size(); x++) {
			char c = line[x];

			int occ_neigh = count_neighbors_p2(lines, x, y);

			if (c == 'L' && occ_neigh == 0) {
				c = '#';
			} else if (c == '#' && occ_neigh >= 5) {
				c = 'L';
			}

			out[y][x] = c;
		}
	}

	return out;
}


int main() {
	std::vector<std::string> lines;
	std::ifstream input{"input"};

	std::string line;
	while(std::getline(input, line))
		lines.push_back(std::move(line));

	long part1 = 0;
	{
		auto state = lines;
		while (true) {
			auto new_state = run_iter_p1(state);

			if (new_state == state)
				break;

			state = new_state;
		}

		for (auto &s : state)
			part1 += std::count(s.begin(), s.end(), '#');
	}

	long part2 = 0;
	{
		auto state = lines;
		while (true) {
			auto new_state = run_iter_p2(state);

			if (new_state == state)
				break;

			state = new_state;
		}

		for (auto &s : state)
			part2 += std::count(s.begin(), s.end(), '#');
	}

	std::cout << "Part 1 - " << part1 << std::endl;
	std::cout << "Part 2 - " << part2 << std::endl;
}
