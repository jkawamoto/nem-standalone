#!/bin/bash
case "$1" in
  nis)
    # Start NIS.
    cd /root/package
    sed -i "s/nem.httpPort/#nem.httpPort/g" nis/config.properties
    echo "nem.httpPort = $PORT" >> nis/config.properties

    ./nix.runNis.sh
    ;;
  ncc)
    # Start NCC
    cd /root/package
    ADDR=$(env | grep "_PORT=tcp:" | head -1)
		IPPORT=${ADDR#*//}

    socat TCP-LISTEN:7890,fork,reuseaddr TCP:${IPPORT} &
    ./nix.runNcc.sh
    ;;
  *)
    # otherwise, execute bash for debugging.
    exec /bin/bash
esac
