#!/bin/bash
#!/bin/bash


date=$(date '+%Y/%m/%d')
uuid=$(uuidgen)
cd  ~/myine/setup_automation_script/
git add timetable_12_december
git add resources.md
git commit -m "update timetable ${date}-${uuid}"

#git push origin main


git push origin main

