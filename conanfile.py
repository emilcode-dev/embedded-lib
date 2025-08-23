from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout


class EmbeddedLibRecipe(ConanFile):
name = "embedded-lib"
version = "0.1.0"
settings = "os", "arch", "compiler", "build_type"
exports_sources = "CMakeLists.txt", "src/*", "include/*"


def layout(self):
cmake_layout(self)


def generate(self):
tc = CMakeToolchain(self)
tc.generate()
deps = CMakeDeps(self)
deps.generate()


def build(self):
cmake = CMake(self)
cmake.configure()
cmake.build()


def package(self):
cmake = CMake(self)
cmake.install()


def package_info(self):
self.cpp_info.libs = ["embedded-lib"]