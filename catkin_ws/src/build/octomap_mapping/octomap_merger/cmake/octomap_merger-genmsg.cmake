# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "octomap_merger: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ioctomap_merger:/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg;-Inav_msgs:/opt/ros/noetic/share/nav_msgs/cmake/../msg;-Ioctomap_msgs:/opt/ros/noetic/share/octomap_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/noetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(octomap_merger_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg" NAME_WE)
add_custom_target(_octomap_merger_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "octomap_merger" "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg" "std_msgs/Header:octomap_msgs/Octomap"
)

get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg" NAME_WE)
add_custom_target(_octomap_merger_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "octomap_merger" "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg" "std_msgs/Header:octomap_msgs/Octomap:octomap_merger/OctomapArray"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/octomap_merger
)
_generate_msg_cpp(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg;/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/octomap_merger
)

### Generating Services

### Generating Module File
_generate_module_cpp(octomap_merger
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/octomap_merger
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(octomap_merger_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(octomap_merger_generate_messages octomap_merger_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_cpp _octomap_merger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_cpp _octomap_merger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(octomap_merger_gencpp)
add_dependencies(octomap_merger_gencpp octomap_merger_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS octomap_merger_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/octomap_merger
)
_generate_msg_eus(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg;/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/octomap_merger
)

### Generating Services

### Generating Module File
_generate_module_eus(octomap_merger
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/octomap_merger
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(octomap_merger_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(octomap_merger_generate_messages octomap_merger_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_eus _octomap_merger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_eus _octomap_merger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(octomap_merger_geneus)
add_dependencies(octomap_merger_geneus octomap_merger_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS octomap_merger_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/octomap_merger
)
_generate_msg_lisp(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg;/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/octomap_merger
)

### Generating Services

### Generating Module File
_generate_module_lisp(octomap_merger
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/octomap_merger
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(octomap_merger_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(octomap_merger_generate_messages octomap_merger_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_lisp _octomap_merger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_lisp _octomap_merger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(octomap_merger_genlisp)
add_dependencies(octomap_merger_genlisp octomap_merger_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS octomap_merger_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/octomap_merger
)
_generate_msg_nodejs(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg;/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/octomap_merger
)

### Generating Services

### Generating Module File
_generate_module_nodejs(octomap_merger
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/octomap_merger
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(octomap_merger_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(octomap_merger_generate_messages octomap_merger_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_nodejs _octomap_merger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_nodejs _octomap_merger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(octomap_merger_gennodejs)
add_dependencies(octomap_merger_gennodejs octomap_merger_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS octomap_merger_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/octomap_merger
)
_generate_msg_py(octomap_merger
  "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/octomap_msgs/cmake/../msg/Octomap.msg;/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/octomap_merger
)

### Generating Services

### Generating Module File
_generate_module_py(octomap_merger
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/octomap_merger
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(octomap_merger_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(octomap_merger_generate_messages octomap_merger_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapArray.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_py _octomap_merger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lajos/catkin_ws/src/octomap_mapping/octomap_merger/msg/OctomapNeighbors.msg" NAME_WE)
add_dependencies(octomap_merger_generate_messages_py _octomap_merger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(octomap_merger_genpy)
add_dependencies(octomap_merger_genpy octomap_merger_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS octomap_merger_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/octomap_merger)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/octomap_merger
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET nav_msgs_generate_messages_cpp)
  add_dependencies(octomap_merger_generate_messages_cpp nav_msgs_generate_messages_cpp)
endif()
if(TARGET octomap_msgs_generate_messages_cpp)
  add_dependencies(octomap_merger_generate_messages_cpp octomap_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/octomap_merger)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/octomap_merger
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET nav_msgs_generate_messages_eus)
  add_dependencies(octomap_merger_generate_messages_eus nav_msgs_generate_messages_eus)
endif()
if(TARGET octomap_msgs_generate_messages_eus)
  add_dependencies(octomap_merger_generate_messages_eus octomap_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/octomap_merger)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/octomap_merger
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET nav_msgs_generate_messages_lisp)
  add_dependencies(octomap_merger_generate_messages_lisp nav_msgs_generate_messages_lisp)
endif()
if(TARGET octomap_msgs_generate_messages_lisp)
  add_dependencies(octomap_merger_generate_messages_lisp octomap_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/octomap_merger)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/octomap_merger
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET nav_msgs_generate_messages_nodejs)
  add_dependencies(octomap_merger_generate_messages_nodejs nav_msgs_generate_messages_nodejs)
endif()
if(TARGET octomap_msgs_generate_messages_nodejs)
  add_dependencies(octomap_merger_generate_messages_nodejs octomap_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/octomap_merger)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/octomap_merger\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/octomap_merger
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET nav_msgs_generate_messages_py)
  add_dependencies(octomap_merger_generate_messages_py nav_msgs_generate_messages_py)
endif()
if(TARGET octomap_msgs_generate_messages_py)
  add_dependencies(octomap_merger_generate_messages_py octomap_msgs_generate_messages_py)
endif()
