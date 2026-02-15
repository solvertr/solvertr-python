# Solvertr API Examples

This repository contains sample code demonstrating how to use the [Solvertr](https://solver.tr) Turnstile APIs.

## API Overview

The Solvertr API provides the Cloudflare Turnstile solution. The following endpoints are available to customers:

| Endpoint | Method | Description |
|----------|--------|----------|
| `/v1/turnstile/solve` | GET, POST | Turnstile solution; returns `token` |
| `/v1/balance` | GET | Balance (number of tokens) |
| `/v1/usage-stats` | GET | Usage statistics (`?days=7`) |
| `/v1/rate-limit-status` | GET | Rate limit status |
| `/v1/status` | GET | API status (no authentication required) |

### Authentication

The API key can be provided in three ways:

- Query parameter: `?apikey=YOUR_API_KEY`
- Header: `X-API-Key: YOUR_API_KEY`
- POST body (JSON): `“apiKey”: “YOUR_API_KEY”`

### Solve Request

- **Required parameters:** `url` (site address), `sitekey` (Turnstile site key)
- **Optional:** `action`, `cdata`
- **Successful response (JSON):** `{ “success”: true, “token”: “...”, “requestId”, ‘balance’, “responseTime” }`
- **Plain text token:** If `txt=true` or `format=txt` is used in the request, the response will only contain the token string (`text/plain`).

## Base URL and API Key

- **Base URL:** `https://api.solver.tr` (production)
- **API Key:** Obtained from the customer panel (dashboard). The environment variable `SOLVERTR_API_KEY` can be used in examples.

## Language Examples

- **[Python](python/)** – Installation, client usage, and example scripts (GET/POST solve, balance, usage-stats, full flow)


Translated with DeepL.com (free version)



#TR

# Solvertr API Örnekleri

Bu depo, [Solvertr](https://solver.tr) Turnstile API'lerinin nasıl kullanılacağını gösteren örnek kodları içerir.

## API Özeti

Solvertr API'si Cloudflare Turnstile çözümü sunar. Aşağıdaki endpoint'ler müşteriye açıktır:

| Endpoint | Method | Açıklama |
|----------|--------|----------|
| `/v1/turnstile/solve` | GET, POST | Turnstile çözümü; `token` döner |
| `/v1/balance` | GET | Bakiye (token sayısı) |
| `/v1/usage-stats` | GET | Kullanım istatistikleri (`?days=7`) |
| `/v1/rate-limit-status` | GET | Rate limit durumu |
| `/v1/status` | GET | API durumu (kimlik gerekmez) |

### Kimlik Doğrulama

API key üç şekilde verilebilir:

- Query parametresi: `?apikey=YOUR_API_KEY`
- Header: `X-API-Key: YOUR_API_KEY`
- POST body (JSON): `"apiKey": "YOUR_API_KEY"`

### Solve İsteği

- **Zorunlu parametreler:** `url` (site adresi), `sitekey` (Turnstile site key)
- **Opsiyonel:** `action`, `cdata`
- **Başarılı yanıt (JSON):** `{ "success": true, "token": "...", "requestId", "balance", "responseTime" }`
- **Düz metin token:** İstekte `txt=true` veya `format=txt` kullanılırsa yanıt sadece token string olur (`text/plain`).

## Base URL ve API Key

- **Base URL:** `https://api.solver.tr` (production)
- **API Key:** Müşteri panelinden (dashboard) alınır. Örneklerde ortam değişkeni `SOLVERTR_API_KEY` kullanılabilir.

## Dil Örnekleri

- **[Python](python/)** – Kurulum, client kullanımı ve örnek script'ler (GET/POST solve, balance, usage-stats, full flow)

## Lisans

Bu örnek kodlar referans amaçlıdır; projenize uygun şekilde kullanabilirsiniz.
