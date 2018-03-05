#!/bin/bash

set -e

get_num_running_procs() {
    num_processes = `ps auxww | grep sleeper | wc -l`

    return $num_processes
}

spawn_cmd() {
    cmd=$1
    
    while [ $( get_num_running_procs ) -gt `nproc` ]; do
        sleep 60
        
    done

    bash $cmd &
}              

main() {

    for s in 1 2 3 4 5
    do
        ./sleeper.sh $s
    done

}


main
