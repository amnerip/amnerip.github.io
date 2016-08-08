#!/usr/bin/env bash

# starts the local server, cds into the 
# directory of the website

CODE_DIR=${HOME}/projects/website
JEKYLL=$(which jekyll)
LOG=localhost-output.log
STOP_SCRIPT=stop-dev.sh

cd "${CODE_DIR}"
${JEKYLL} serve &> ${LOG} &

echo "run 'stop.sh' to stop the development server."
echo "server logs: "${LOG}
echo "#!/usr/bin/env bash" > ${STOP_SCRIPT}
echo "kill" $! >> ${STOP_SCRIPT}

chmod +x ${STOP_SCRIPT}
