# Voice Agent Infrastructure Challenge

Infrastructure platform behind a Vapi-based Voice Agent backend — a reliable,
observable, and reproducible deployment demonstrating practical DevOps
capabilities: containerization, cloud deployment, reverse proxy + HTTPS,
monitoring, backup automation, health checks, CI/CD validation, and webhook
integration.

The backend is built with **FastAPI** and **PostgreSQL**, fully containerized
with **Docker Compose**, and deployed on **AWS EC2** behind **Nginx + HTTPS**
via a DuckDNS domain.

---

## Architecture

```
                    Vapi Voice Agent
                          |
                     HTTPS Webhook
                          |
                          ▼
              agent-voice.duckdns.org
                          |
                Nginx Reverse Proxy
                  (SSL Termination)
                          |
                          ▼
             FastAPI Backend Container
                     Port 8000
                          |
                          ▼
              PostgreSQL 16 Container
                          |
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
  Backup Automation                  Monitoring Stack
  - Postgres dumps                   - Prometheus
  - Restore scripts                  - Grafana
                                      - Alertmanager
```

---

## Production Deployment

| Component       | Technology     |
| --------------- | -------------- |
| Cloud Provider  | AWS EC2        |
| OS              | Amazon Linux   |
| Domain          | DuckDNS        |
| Reverse Proxy   | Nginx          |
| SSL Certificate | Let's Encrypt  |
| Backend Runtime | FastAPI        |
| Database        | PostgreSQL 16  |
| Containers      | Docker         |
| Orchestration   | Docker Compose |

---

## Technologies Used

**Application:** Python, FastAPI, SQLAlchemy, PostgreSQL

**Infrastructure:** Docker, Docker Compose, Nginx, Prometheus, Grafana, Alertmanager

**Automation:** GitHub Actions, shell scripting, backup scripts

---

## Features

**Backend**

- FastAPI REST API
- Vapi webhook endpoint
- PostgreSQL database integration via SQLAlchemy ORM
- CRUD operations
- Health monitoring endpoint
- Prometheus metrics endpoint

**Infrastructure**

- Dockerized services
- Persistent database storage
- Environment-based configuration
- Reverse proxy setup
- HTTPS deployment
- Monitoring stack
- Database backup and restore automation

---

## Live Deployment

**Production URL:** `https://agent-voice.duckdns.org`

**Health check**

```
GET https://agent-voice.duckdns.org/health
```

```json
{
  "status": "healthy",
  "service": "voice-agent-backend"
}
```

**API documentation (Swagger UI)**

```
https://agent-voice.duckdns.org/docs
```

**Vapi webhook URL**

```
POST https://agent-voice.duckdns.org/webhook
```

### API Endpoints

| Endpoint   | Method | Description                |
| ---------- | ------ | -------------------------- |
| `/`        | GET    | Application status         |
| `/health`  | GET    | Health check               |
| `/metrics` | GET    | Prometheus metrics         |
| `/webhook` | POST   | Receive voice agent events |

---

## Running Locally

**1. Clone the repository**

```bash
git clone <repository-url>
cd voice-agent-infra
```

**2. Configure environment variables**

Create a `.env` file:

```env
POSTGRES_DB=voice_agent
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
```

**3. Start services**

```bash
docker compose up -d
```

**4. Verify containers**

```bash
docker ps
```

Expected services: `voice-backend`, `postgres-db`

**5. Local URLs**

- Backend: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`

---

## AWS Deployment

```
Developer
    |
GitHub Repository
    |
AWS EC2
    |
Docker Compose
    |
FastAPI + PostgreSQL
```

**Deployment steps**

```bash
# SSH into EC2
ssh -i <key.pem> ec2-user@<EC2-IP>

# Clone repository
git clone <repository-url>
cd voice-agent-infra

# Start services
docker compose up -d

# Verify
docker ps
```

---

## Nginx Reverse Proxy

Nginx handles incoming HTTPS traffic and forwards requests to FastAPI.

```
Client
   |
HTTPS :443
   |
Nginx
   |
FastAPI Container :8000
```

### HTTPS Configuration

SSL certificates are generated using **Certbot** + **Let's Encrypt**.

Certificate renewal test:

```bash
sudo certbot renew --dry-run
```

---

## Monitoring

The project includes a full monitoring stack.

**Prometheus** — collects metrics from `/metrics`, including application
health, request metrics, and runtime information.

**Grafana** — provides dashboards for visualization (API performance,
request rate, system health).

Default credentials: `admin` / `admin` _(change before any real production use)_

**Alertmanager** — configuration included for future alert routing (email,
Slack, PagerDuty). Currently a placeholder receiver — see Limitations below.

---

## Backup Strategy

Database backups are handled through automation scripts.

**Create a backup**

```bash
./backups/backup.sh
```

**Restore a backup**

```bash
./backups/restore.sh backups/<backup-file>.sql
```

This provides database recovery, disaster recovery capability, and data
portability.

---

## CI/CD

GitHub Actions validates the project automatically. Pipeline includes:

- Docker Compose validation
- Application build verification
- Configuration checks

**Future improvements:** Docker image publishing, automated deployment, security scanning.

---

## Security

**Implemented**

- Environment variables for secrets
- Docker isolation
- HTTPS encryption
- Reverse proxy protection
- Secure webhook endpoint

**Production improvements planned**

- AWS Secrets Manager
- IAM-based access control
- Encryption at rest
- Network segmentation
- Audit logging
- Centralized security monitoring

---

## Repository Structure

```
voice-agent-infra/
├── app/
│   ├── FastAPI application
│   └── Dockerfile
│
├── backups/
│   ├── backup.sh
│   └── restore.sh
│
├── monitoring/
│   ├── prometheus/
│   ├── grafana/
│   └── alertmanager/
│
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
│
├── scripts/
│
├── .github/
│   └── workflows/
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Design Decisions & Trade-offs

Given the limited implementation timeframe, priority was given to:

- Reliability
- Observability
- Reproducibility
- Operational readiness

**Docker Compose was chosen over Kubernetes** because the workload is
single-node, deployment simplicity mattered more at this scale, and the
infrastructure stays easy to reproduce.

### Current Limitations

- Single EC2 instance — no horizontal scaling
- No authentication layer on API endpoints
- Alertmanager receiver is a placeholder (not yet wired to a real channel)
- No automated database migrations

### Future Improvements

- Terraform infrastructure provisioning
- Kubernetes deployment / AWS ECS or EKS migration
- GitHub Container Registry for image publishing
- Fully automated deployment pipeline
- Alembic database migrations
- Centralized logging (e.g. AWS CloudWatch)
- Load balancing and Auto Scaling Groups
- High-availability architecture

---

## Conclusion

This project demonstrates a complete DevOps workflow for deploying a Voice
Agent backend:

- ✔ FastAPI backend
- ✔ PostgreSQL database
- ✔ Docker containerization
- ✔ AWS EC2 deployment
- ✔ Nginx reverse proxy
- ✔ HTTPS with Let's Encrypt
- ✔ Vapi webhook integration
- ✔ Monitoring strategy
- ✔ Backup automation
- ✔ CI/CD validation

The result is a reproducible, observable, and production-oriented
infrastructure platform suitable for a Voice Agent system.
