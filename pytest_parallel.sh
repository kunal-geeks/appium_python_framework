#!/bin/bash

echo "Starting parallel execution (emulator + real device)!!!"

mkdir -p reports

TARGET_DEVICE=emulator python -m pytest -n 1 -vv \
  --html=reports/emulator_report.html \
  --self-contained-html &
PID1=$!

TARGET_DEVICE=real python -m pytest -n 1 -vv \
  --html=reports/real_device_report.html \
  --self-contained-html &
PID2=$!

wait $PID1 $PID2

echo "Parallel execution completed!!!"
echo "Emulator report: reports/emulator_report.html!!!"
echo "Real device report: reports/real_device_report.html!!!"
