#!/bin/bash
isort ./attendance && black ./attendance
isort ./test/attendance && black ./test/attendance
isort ./app.py && black ./app.py