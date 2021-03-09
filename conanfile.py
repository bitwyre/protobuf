from conans import ConanFile, CMake


class ProtobufConan(ConanFile):
    name = "protobuf"
    version = "3.11.4"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Protobuf here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "use_pic": [True, False]
    }
    default_options = {"shared": False, "use_pic": False}
    requires = [
        "zlib/1.2.11@bitwyre/stable"
    ]
    generators = "cmake"
    exports_sources = "*"
    no_copy_source = True

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.definitions['BUILD_TESTING'] = False
        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.use_pic
        cmake.definitions['protobuf_BUILD_CONFORMANCE'] = False
        cmake.definitions['protobuf_BUILD_EXAMPLES'] = False
        cmake.definitions['protobuf_DEBUG_POSTFIX'] = ""
        cmake.definitions['protobuf_BUILD_PROTOC_BINARIES'] = True
        cmake.definitions['protobuf_BUILD_SHARED_LIBS'] = False
        cmake.definitions['protobuf_BUILD_TESTS'] = False
        cmake.definitions['ZLIB_ROOT'] = self.deps_cpp_info["zlib"].rootpath
        cmake.configure(source_folder='cmake')
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["protobuf"]
