#!/usr/bin/env bash

set -e

PWD=$(pwd)

if [[ $PWD == "$GOPATH"/src/* ]] ;
then
	PROJECT=${PWD#"$GOPATH"/src/*}
	echo "run fmt and goimports for $PROJECT"

	gofmt -w `find . -name '*.go' | grep -v vendor`

	goimports -w -local='$PROJECT' `find . -name '*.go' | grep -v vendor`

	exit 0
fi

echo "$PWD is not GOPATH"
exit 1

