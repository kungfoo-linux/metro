[collect ./common.spec]

[section source]

: stage2
base: $[]-$[:subarch]-$[:build]-$[:version]
name: $[]-$[:subarch]-$[:build]-$[:version]-$[:count]
build: $[target/build]
subarch: $[target/subarch]
version: $[target/version]
count: $[target/count]
