#!/bin/bash
source $HOME/housemonitor/init_credentials
source $HOME/housemonitor/.venv/bin/activate
cd $HOME/housemonitor
python -m housemonitor.measure_and_save
date >> $HOME/tmp/tmp.log
