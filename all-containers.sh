#/bin/sh

for f in * ; do
    if [ -d "$f" ] && [ -f "$f/docker-compose.yml" ]; then
	    cd $f;
	    docker-compose $1;
	    cd ..;
    fi
done
