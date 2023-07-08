# Git contribution time

requires `python >= 3.10`

## Install
`pip install git_time`

## Usage
It's simple: `get-contribution` in a Git Repository.

Additionally, you can add an *optional* argument to specifiy the contribution of which user. Like so `get-contribution 'John Doe'` 

## Algorithms
The algorithm is very simple. It calculates your time spent a given repo based on the number of times you have pushed to it.
The time between your "pushes" is the contribution time.

It is not meant to be *accurate*, rather, it is meant to give you a *sense* of how much time you or someone else has spent on a project.

Some people might find this *sense* of time useful. 
For example: folks who are looking for jobs and need a metric.

