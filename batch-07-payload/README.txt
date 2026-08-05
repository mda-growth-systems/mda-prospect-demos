Batch 07 payload reconstruction instructions

The files in batch-07-payload are ordered Base64 segments of a gzip-compressed tar archive. The GitHub Pages deployment workflow reconstructs and extracts the ten prospect folders, verifies the public pages, then removes this temporary payload from the repository.
