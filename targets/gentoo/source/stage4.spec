[collect ./common.spec]

[section source]

: stage4
base: $[]-$[:subarch]-$[:build]-$[:version]
name: $[]-$[:subarch]-$[:build]-$[:version]-$[:count]
build: $[target/build]
subarch: $[target/subarch]
version: << $[path/mirror/target/control]/version/stage4
count: << $[path/mirror/target/control]/version/count
