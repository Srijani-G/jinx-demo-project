"""Active health-check poller for the API gateway load balancer pool."""
import httpx


def check(targets):
    healthy = []
    for t in targets:
        try:
            if httpx.get(f"http://{t}/healthz", timeout=2).status_code == 200:
                healthy.append(t)
        except httpx.HTTPError:
            pass
    return healthy