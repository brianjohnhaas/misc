#!/bin/bash

set -ex

num_running=0

get_num_running_procs() {
    num_running=`ps auxww | grep sleeper | wc -l`

    echo "num running procs: $num_running"
}

spawn_cmd() {
    echo "spawn_cmd()"
    
    cmd=$1

    get_num_running_procs
    
    while [ $num_running -gt `nproc` ]
    do
        sleep 60
        get_num_running_procs
    done

    echo "spawning CMD: $cmd"
    bash $cmd &
}              

main() {
    echo 'main()'
    
    for s in 1 2 3 4 5
    do
        echo "Spawning $s"
        spawn_cmd "./sleeper.sh $s"
    done

    wait
    
    echo "done"
    
    exit 0
}


main
