#!/usr/bin/env Rscript

#scriptdir = getSrcDirectory(function(x) {x})

scriptdir <- dirname(sys.frame(1)$ofile)
message("ScriptDir: ", scriptdir)


main = function() {

    suppressPackageStartupMessages(library("argparse"))
    parser = ArgumentParser()
    parser$add_argument("--numA", help="numA", type="integer", required=TRUE, nargs=1)
    parser$add_argument("--numB", help="numB", type="integer", required=TRUE, nargs=1)

    args = parser$parse_args()

    x = addme(11,20)
    message("11 + 20 = ", x)
    
    message(args$numA, "+", args$numB, "=", addme(args$numA, args$numB))
        
}


addme = function(a, b) {

    return(a+b);
}

test.addme = function() {
    checkEquals(addme(1,2), 3)
    checkEquals(addme(4,5), 9)
}



if (interactive()) {
    main()
}


