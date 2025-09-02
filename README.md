## EmbeddedLib: Generic Embedded Software Library
[![Tests](https://github.com/emilcode-dev/embedded-lib/actions/workflows/build-test.yml/badge.svg)](https://github.com/emilcode-dev/embedded-lib/actions/workflows/build-test.yml)
[![Build Devcontainer Image](https://github.com/emilcode-dev/embedded-lib/actions/workflows/devcontainer.yml/badge.svg)](https://github.com/emilcode-dev/embedded-lib/actions/workflows/devcontainer.yml)
[![Build and Deploy Docs](https://github.com/emilcode-dev/embedded-lib/actions/workflows/build-and-publish-doc.yml/badge.svg)](https://github.com/emilcode-dev/embedded-lib/actions/workflows/build-and-publish-doc.yml)

EmbeddedLib is a modular C/C++ library designed for embedded software projects. It provides reusable components, build/test automation with CMake, and packaging via Conan. The repository supports both development and production builds, integrates with JFrog Artifactory for package management, and includes documentation generation tools. This project aims to streamline embedded development workflows and promote code reuse across projects.

### Developer guide

* run docker
* run dev container in vs code
* build project

```
mkdir build && cd build
```

- test build:

```
cmake -DTARGET_GROUP=test .. 
cmake --build .
ctest
```

- production build:

```
cmake -DTARGET_GROUP=production ..
cmake --build .
```

### JFrog configuration 
<jfrog-artifactory-token>

#### Add artifactory repository to client configuration
```
conan remote add emilcode-conan https://emilcodedev.jfrog.io/artifactory/api/conan/emilcode-conan
```

#### Login to the artifactory (Conan V2.x and up), client documentation found here: docs.conan.io

```
conan remote login -p <jfrog-artifactory-token> emilcode-conan <username/email>
```

### JFrog Upload
Upload a Conan (Conan 2) recipe and its binary packages using the following command:

```
conan upload "*" --remote=emilcode-conan --confirm
```

<RECIPE> is the Conan recipe reference you want to upload in the format: <NAME>/<VERSION>@<USER>/<CHANNEL>
For example: lib/1.0@conan/stable


### Build library

```
conan profile detect --name=profile_build_detected
conan install . --build missing --profile:build=profile_build_detected --profile:host=profile_build_detected 
```

#### Activate the build environment so that we use the selected CMake version for building

```
source build/Release/generators/conanbuild.sh
```

#### Build our application

```
cmake --preset=conan-release
cmake --build --preset=conan-release
```

### Build and Run Unittests

Unity is used in this project as unittesting framework.

```
mkdir build && cd build
cmake -DTARGET_GROUP=test ..
cmake --build .
ctest
```

### Create documentation

```
cd doc
doxygen Doxyfile
sphinx-build ./source ./build
```

### Outlook

- [ ] Extend READMe.md
- [ ] Publish package to another remote after jfrog trial has expired