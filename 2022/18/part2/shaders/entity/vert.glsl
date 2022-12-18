#version 330

layout(location = 0) in vec3 vertex_position;
layout(location = 1) in vec3 tex_coords;
layout(location = 2) in vec3 normal;

out vec3 local_position;
out vec3 interpolated_tex_coords;
out float shading;

uniform mat4 transform_matrix;
uniform mat4 matrix;

void main(void) {
	local_position = vertex_position;

	interpolated_tex_coords = tex_coords;

	vec3 adjusted_normal = (vec4(normal, 1.0) * transform_matrix).xyz;
	vec3 sunlight = vec3(0.0, 0.0, 1.0);

	shading = 1.0 - 0.4 * abs(dot(normalize(adjusted_normal), normalize(sunlight)));

	gl_Position = matrix * vec4(vertex_position, 1.0);
}
