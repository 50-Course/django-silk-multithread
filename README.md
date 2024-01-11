To reproduce issue where silk will only profile the first of several concurrent long-running requests:

- access both `/basic/` and `/basic/second/` at the same time.
- then view the requests summaries in `silk` - only one of them will have profiling information.
