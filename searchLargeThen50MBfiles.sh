#!/bin/bash

echo  "即将查询超过50MB的文件列表,结果呈现如下:"

find . -type f -size +50M