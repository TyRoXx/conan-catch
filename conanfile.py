from os import unlink
from os.path import join
from conans import CMake, ConanFile
from conans.tools import download, unzip, check_sha256


class Catch(ConanFile):
    name = "catch"
    version = "1.5.6"
    branch = "stable"
    license = "Boost"
    url="http://github.com/TyRoXx/conan-catch"

    ZIP_FOLDER_NAME = "Catch-{0}".format(version)
    ZIP_URL_NAME = 'v{0}.zip'.format(version)
    FILE_SHA = '6c303fba75a949c2693ad85f6c604f06396622e2e83e54cdb3c6f6f9926cb758'

    def source(self):
        zip_name = "catch.zip"
        download("https://github.com/philsquared/Catch/archive/%s" % self.ZIP_URL_NAME, zip_name)
        check_sha256(zip_name, self.FILE_SHA)
        unzip(zip_name)
        unlink(zip_name)

    def package(self):
        self.copy("catch.hpp", "include", join(self.ZIP_FOLDER_NAME, 'single_include'))
        self.copy("catch_with_main.hpp", "include", join(self.ZIP_FOLDER_NAME, 'include'))

    def package_info(self):
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
