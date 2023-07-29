#!/bin/sh

git config --global --add safe.directory /github/workspace
git config --global user.email "noreply@github.com"
git config --global user.name "Github Actions[bot/notes-assistant]"

year=$(date +'%Y')
month=$(date +'%m')
quarter=""
if [ $month -le 3 ]; then
    quarter="${year}Q1"
elif [ $month -gt 3 ] && [ $month -le 6 ]; then
    quarter="${year}Q2"
elif [ $month -gt 6 ] && [ $month -le 9 ]; then
    quarter="${year}Q3"
elif [ $month -gt 9 ] && [ $month -le 12 ]; then
    quarter="${year}Q4"
fi
branchName="openai-assistant/${quarter}"
commitMessage="Summarize ${quarter}"
python3 main.py --assistant $2 --file $3 --output $4
git checkout "${branchName}" || git checkout -b "${branchName}"
git add $1
git commit --message "${commitMessage}}"
git push origin "${branchName}"
gh pr create --assignee "@jmoney" --reviewer "@jmoney" --title "Summarizing ${quarter}" --body "${commitMessage}"