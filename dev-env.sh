#!/usr/bin/env bash
# starts the local server, cds into the 
# directory of the website

CODE_DIR=${HOME}/projects/website
JEKYLL=$(which jekyll)
LOG=localhost-output.log
STOP_SCRIPT=stop-dev.sh

cd "${CODE_DIR}"

# Look for running instances of jekyll in the background.
ps cax | grep jekyll &> /dev/null

if [[ $? -eq 0 ]]; then
  echo "Server is already running:"
  ps cax | grep jekyll
else
  ${JEKYLL} serve &> ${LOG} &

  echo "\
  #!/usr/bin/env bash
  kill $!" > ${STOP_SCRIPT}

  chmod +x ${STOP_SCRIPT}
fi

echo "\
run ${STOP_SCRIPT} to stop the development server.
server logs: ${LOG}"

