VERSION := 0.0.1

DIST_DIR := ./dist

put-readme:
	find npm/ -type d -name 'lefthook*' -exec cp -f ./README.md \{} \;

clean:
	find pyenv/ -type f -name 'README.md' -exec rm \{} \;
	find pyenv/ -type f -name 'lefthook*' -exec rm \{} \;