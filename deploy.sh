#!/usr/bin/env bash
# Deploy site/ to SiteGround over SSH (rsync). Staging by default.
#   ./deploy.sh              -> staging
#   ./deploy.sh --production -> live site (asks for confirmation)
set -euo pipefail
cd "$(dirname "$0")"
set -a; . ./.env; set +a

python3 build_site.py >/dev/null

TARGET="$SG_REMOTE_PATH_STAGING"; LABEL="staging ($STAGING_DOMAIN)"
if [ "${1:-}" = "--production" ]; then
  [ -n "${SG_REMOTE_PATH_PRODUCTION:-}" ] || { echo "SG_REMOTE_PATH_PRODUCTION is empty in .env"; exit 1; }
  TARGET="$SG_REMOTE_PATH_PRODUCTION"; LABEL="PRODUCTION ($PRODUCTION_DOMAIN)"
  read -r -p "Deploy to $LABEL? Type 'yes': " ans; [ "$ans" = "yes" ] || { echo "Cancelled."; exit 1; }
fi

echo "Deploying site/ to $LABEL"
rsync -avz --exclude '.DS_Store' \
  -e "ssh -i $SG_SSH_KEY_PATH -p $SG_SSH_PORT -o IdentitiesOnly=yes" \
  site/ "$SG_SSH_USER@$SG_SSH_HOST:$TARGET/"
echo "Done."
