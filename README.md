# 🅿️ Parking Service - API de Estacionamento

> Sistema robusto e escalável de gerenciamento de estacionamento desenvolvido com Django, DRF e boas práticas de arquitetura backend.

[![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0.4-darkgreen?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.17.1-red?style=flat-square)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=flat-square&logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?style=flat-square&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Tecnologias](#tecnologias)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Funcionalidades](#funcionalidades)
- [Roadmap](#roadmap)
- [Como Executar](#como-executar)
- [Endpoints Principais](#endpoints-principais)
- [Autenticação](#autenticação)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Boas Práticas Aplicadas](#boas-práticas-aplicadas)
- [Possíveis Melhorias](#possíveis-melhorias)
- [Contato](#contato)

---

## 🎯 Visão Geral

O **Parking Service** é uma API REST completa para gerenciamento de estacionamentos, desenvolvida do zero com foco em boas práticas de desenvolvimento backend, segurança, escalabilidade e performance.

O sistema oferece controle administrativo total sobre clientes, veículos, vagas de estacionamento e registros de entrada/saída, com uma API moderna e segura que permite integrações externas.

**Fluxo do Sistema:** [Visualizar no Whimsical](https://whimsical.com/parking-service-SSoifu29a1MVLAmLAPMk2a)

---

## 🛠️ Tecnologias

### Backend & Framework
- **Python 3.13** - Linguagem de programação
- **Django 6.0.4** - Framework web robusto
- **Django REST Framework 3.17.1** - Criação de APIs REST
- **Django Jazzmin 3.0.4** - Interface administrativa moderna

### Autenticação & Segurança
- **JWT (PyJWT 2.12.1)** - Autenticação stateless
- **djangorestframework-simplejwt 5.5.1** - Implementação JWT integrada
- **Permissões granulares** - Controle de acesso por nível

### Banco de Dados
- **PostgreSQL 15** - SGBD robusto e escalável
- **psycopg2-binary 2.9.12** - Adaptador Python para PostgreSQL

### Processamento Assíncrono
- **Celery 5.6.3** - Fila de tarefas distribuída
- **RabbitMQ 4.0** - Message Broker

### Filtros & Documentação
- **django-rql 4.4.1** - Filtros avançados com RQL
- **drf-spectacular** - Geração automática de OpenAPI (Swagger)

### Containerização
- **Docker** - Containerização
- **Docker Compose** - Orquestração local

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Application                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌────────────────────────────────────────────────────────┐  │
│  │           Django REST Framework API                    │  │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │  │
│  │  │ Views/       │ │ Serializers  │ │ Permissions  │   │  │
│  │  │ ViewSets     │ │              │ │ & Filters    │   │  │
│  │  └──────────────┘ └──────────────┘ └──────────────┘   │  │
│  └────────────────────────────────────────────────────────┘  │
│                          │                                    │
│  ┌────────────────────────────────────────────────────────┐  │
│  │              Modelos de Negócio                        │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐               │  │
│  │  │ Customer │ │ Vehicle  │ │ Parking  │               │  │
│  │  │          │ │          │ │ Spot     │               │  │
│  │  └──────────┘ └──────────┘ └──────────┘               │  │
│  │  ┌──────────────────┐                                  │  │
│  │  │ Parking Record   │                                  │  │
│  │  │ (Entry/Exit)     │                                  │  │
│  │  └──────────────────┘                                  │  │
│  └────────────────────────────────────────────────────────┘  │
│                          │                                    │
│  ┌────────────────────────────────────────────────────────┐  │
│  │    Processamento Assíncrono (Celery + RabbitMQ)       │  │
│  │  ├─ Auto-complete de dados via placa                  │  │
│  │  ├─ Notificações (WhatsApp, Email)                    │  │
│  │  └─ Tarefas de background                             │  │
│  └────────────────────────────────────────────────────────┘  │
│                          │                                    │
└─────────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   PostgreSQL          RabbitMQ         APIs Externas
   (Persistência)      (Fila)           (Placa Veículo)
```

---

## ✨ Funcionalidades

### 🔐 Sistema de Administração

- ✅ **Controle de Usuários** - Gerenciamento completo de usuários com roles
- ✅ **Gestão de Permissões** - Controle granular de acessos
- ✅ **Dashboard Jazzmin** - Interface administrativa moderna e intuitiva
- ✅ **Auditoria de Ações** - Rastreamento de operações

### 📱 Cadastros Completos

- ✅ **Clientes** - Cadastro, edição e exclusão de clientes
- ✅ **Veículos** - Registro de veículos com dados do cliente
- ✅ **Tipos de Veículos** - Categorização de veículos
- ✅ **Vagas** - Gerenciamento de vagas de estacionamento
- ✅ **Entradas/Saídas** - Registro automático de entrada e saída de veículos

### 🔄 Controle de Vagas

- ✅ **Status Automático** - Vagas atualizadas automaticamente (ocupado/livre)
- ✅ **Relatórios em Tempo Real** - Visualização da ocupação
- ✅ **Histórico de Ocupação** - Rastreamento completo

### 🔌 API REST Completa

- ✅ **CRUD para todas as entidades** - Operações completas de criação, leitura, atualização e exclusão
- ✅ **Autenticação JWT** - Segura e stateless
- ✅ **Filtros Avançados (RQL)** - Busca complexa e flexível
- ✅ **Controle de Acesso** - Clientes visualizam apenas seus dados
- ✅ **Documentação Swagger** - Documentação interativa e atualizada automaticamente

### ⚙️ Processamento Assíncrono

- ✅ **Celery + RabbitMQ** - Processamento de tarefas em background
- ✅ **Auto-complete de Placa** - Busca de dados do veículo em APIs externas
- ✅ **Notificações** - Sistema pronto para integração com WhatsApp e Email

### 🚀 Funcionalidades Avançadas

- ✅ **Containerização** - Docker e Docker Compose configurados
- ✅ **Banco PostgreSQL** - Escalável e confiável
- ✅ **CI/CD Ready** - Pronto para pipelines de automação
- ✅ **Tratamento de Erros** - Respostas HTTP padronizadas


---

## 🚀 Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.13+ (para desenvolvimento local)
- Git

### Instalação com Docker (Recomendado)

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/parking-service.git
cd parking-service
```

2. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

3. **Inicie os containers**
```bash
docker-compose up -d
```

4. **Execute as migrações**
```bash
docker-compose exec parking_service python manage.py migrate
```

5. **Crie um superusuário**
```bash
docker-compose exec parking_service python manage.py createsuperuser
```

6. **Acesse a aplicação**
- API: http://localhost:8000/api/v1/
- Admin: http://localhost:8000/admin/
- Swagger: http://localhost:8000/api/v1/docs/
- Redoc: http://localhost:8000/api/v1/redoc/

### Desenvolvimento Local

1. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure o banco de dados**
```bash
python manage.py migrate
```

4. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

5. **Inicie o servidor**
```bash
python manage.py runserver
```

6. **Inicie o Celery (em outro terminal)**
```bash
celery -A core worker -l info
```

---

## 🔌 Endpoints Principais

### Autenticação

```bash
# Login e obter tokens
POST /api/v1/authentication/token/
{
  "username": "seu_usuario",
  "password": "sua_senha"
}

# Refresh do token
POST /api/v1/authentication/token/refresh/
{
  "refresh": "seu_token_refresh"
}

# Verificar token
POST /api/v1/authentication/token/verify/
{
  "token": "seu_access_token"
}
```

### Clientes

```bash
# Listar clientes
GET /api/v1/customers/

# Criar cliente
POST /api/v1/customers/
{
  "name": "João Silva",
  "cpf": "12345678901",
  "phone": "11999999999"
}

# Detalhes de cliente
GET /api/v1/customers/{id}/

# Atualizar cliente
PUT /api/v1/customers/{id}/

# Deletar cliente
DELETE /api/v1/customers/{id}/
```

### Veículos

```bash
# Listar veículos
GET /api/v1/vehicles/

# Criar veículo
POST /api/v1/vehicles/
{
  "license_plate": "ABC-1234",
  "brand": "Honda",
  "model": "Civic",
  "color": "Prata",
  "vehicle_type": 1
}

# Buscar por placa
GET /api/v1/vehicles/?license_plate=ABC-1234

# Tipos de veículo
GET /api/v1/vehicles/type/
```

### Vagas de Estacionamento

```bash
# Listar vagas
GET /api/v1/parking/spots/

# Vagas disponíveis
GET /api/v1/parking/spots/?is_occupied=false

# Criar vaga
POST /api/v1/parking/spots/
{
  "spot_number": "A-01",
  "is_occupied": false
}
```

### Registros de Entrada/Saída

```bash
# Listar registros
GET /api/v1/parking/records/

# Registrar entrada
POST /api/v1/parking/records/
{
  "vehicle": 1,
  "parking_spot": 1,
  "entry_time": "2024-05-06T10:30:00Z"
}

# Registrar saída
PATCH /api/v1/parking/records/{id}/
{
  "exit_time": "2024-05-06T12:30:00Z"
}
```

### Documentação

```bash
# Swagger UI
GET /api/v1/docs/

# OpenAPI Schema
GET /api/v1/schema/

# Redoc
GET /api/v1/redoc/
```

### Filtros Avançados (RQL)

```bash
# Filtrar veículos por placa
GET /api/v1/vehicles/?filter=license_plate:eq:ABC-1234

# Buscar registros por data
GET /api/v1/parking/records/?filter=entry_time:gte:2024-05-01

# Combinações complexas
GET /api/v1/parking/records/?filter=and(vehicle_id:eq:1;parking_spot_id:eq:1)
```

---

## 🔐 Autenticação

O projeto utiliza **JWT (JSON Web Tokens)** para autenticação segura e stateless.

### Como Funciona

1. **Cliente faz login** enviando credenciais
2. **Servidor retorna dois tokens:**
   - `access_token` - Validade curta (5 minutos)
   - `refresh_token` - Validade longa (24 horas)

3. **Cliente inclui o access_token** em cada requisição no header `Authorization`

### Exemplo de Uso

```bash
# 1. Obter tokens
curl -X POST http://localhost:8000/api/v1/authentication/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "senha123"
  }'

# Resposta
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}

# 2. Usar o access_token
curl -X GET http://localhost:8000/api/v1/customers/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."

# 3. Renovar o token (quando expirar)
curl -X POST http://localhost:8000/api/v1/authentication/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }'
```

### Níveis de Permissão

- **Superusuário** - Acesso total ao sistema
- **Staff** - Acesso administrativo
- **Cliente** - Acesso limitado aos seus próprios dados
- **Anônimo** - Sem acesso à API

---

## 📁 Estrutura de Pastas

```
parking-service/
├── core/                          # Configurações principais
│   ├── settings.py               # Configurações Django
│   ├── urls.py                   # Rotas principais
│   ├── wsgi.py                   # WSGI para produção
│   ├── asgi.py                   # ASGI para websockets
│   ├── celery.py                 # Configuração Celery
│   ├── permissions.py            # Permissões customizadas
│   └── __init__.py
│
├── authentication/               # App de autenticação
│   ├── urls.py                   # Rotas de auth
│   ├── views.py                  # Vistas de autenticação
│   └── migrations/
│
├── customers/                    # App de clientes
│   ├── models.py                 # Modelo de Cliente
│   ├── views.py                  # Endpoints de clientes
│   ├── serializers.py            # Serialização de dados
│   ├── filters.py                # Filtros RQL
│   ├── urls.py                   # Rotas
│   ├── admin.py                  # Admin Jazzmin
│   └── migrations/
│
├── vehicles/                     # App de veículos
│   ├── models.py                 # Modelos (Vehicle, VehicleType)
│   ├── views.py                  # Endpoints de veículos
│   ├── serializers.py            # Serialização
│   ├── filters.py                # Filtros
│   ├── tasks.py                  # Tarefas Celery
│   ├── signals.py                # Sinais Django
│   ├── urls.py                   # Rotas
│   └── migrations/
│
├── parking/                      # App de estacionamento
│   ├── models.py                 # Modelos (ParkingSpot, ParkingRecord)
│   ├── views.py                  # Endpoints
│   ├── serializers.py            # Serialização
│   ├── filters.py                # Filtros
│   ├── signals.py                # Atualização automática de status
│   ├── urls.py                   # Rotas
│   └── migrations/
│
├── static/                       # Arquivos estáticos
│   └── images/
│
├── requirements.txt              # Dependências Python
├── manage.py                     # Gerenciador Django
├── Dockerfile                    # Imagem Docker
├── docker-compose.yml            # Orquestração
└── README.md                     # Este arquivo

```

---

## ⭐ Boas Práticas Aplicadas

### 1. **Arquitetura em Camadas**
- Separação clara entre models, views, serializers e urls
- Cada app tem responsabilidade bem definida

### 2. **Autenticação & Segurança**
- JWT com tokens curtos e refresh tokens
- Permissões granulares por endpoint
- Validação de entrada em todos os serializers
- CORS configurado adequadamente

### 3. **Padrões de Código**
- Uso de ViewSets para reduzir repetição
- Serializers para validação e transformação
- Filtros RQL para queries complexas
- Tratamento de exceções customizado

### 4. **Processamento Assíncrono**
- Celery para tarefas pesadas
- RabbitMQ como broker confiável
- Retry automático em falhas
- Logging de todas as tarefas

### 5. **Banco de Dados**
- Migrações versionadas
- Índices em fields frequentemente consultados
- Relacionamentos bem modelados
- Cascade delete apropriado

### 6. **Documentação**
- Swagger/OpenAPI automático
- Docstrings em modelos e views
- README completo
- Exemplos de uso nos endpoints

### 7. **Containerização**
- Docker com multi-stage (possível otimização)
- Docker Compose para ambiente local
- Volumes para desenvolvimento
- Network isolada

### 8. **Testabilidade**
- Código modular e desacoplado
- Factories para testes
- Fixtures reutilizáveis
- Mock de serviços externos

---

## 🔮 Possíveis Melhorias

### Curto Prazo
- [ ] Testes automatizados (unittest/pytest)
- [ ] Rate limiting por IP/user
- [ ] Cache Redis para queries pesadas
- [ ] Paginação nos endpoints
- [ ] Soft delete para registros

### Médio Prazo
- [ ] Notificações em tempo real (WebSockets)
- [ ] Relatórios em PDF/Excel
- [ ] Integração com gateway de pagamento
- [ ] Backup automático do banco
- [ ] Monitoramento com Prometheus/Grafana

### Longo Prazo
- [ ] Machine Learning para previsão de ocupação
- [ ] App mobile (React Native/Flutter)
- [ ] Geolocalização de vagas
- [ ] QR Code para acesso
- [ ] Sistema de reservas antecipadas

### Performance
- [ ] Otimização de queries N+1
- [ ] Database sharding se necessário
- [ ] CDN para arquivos estáticos
- [ ] Compression GZIP nos responses
- [ ] Connection pooling no PostgreSQL

### DevOps
- [ ] GitHub Actions para CI/CD
- [ ] Deploy automático
- [ ] Kubernetes para orquestração
- [ ] ELK Stack para logging
- [ ] SentryIO para error tracking

---

## 📊 Screenshots & Documentação

### Sugestões de Captura de Telas

1. **Swagger Documentation**
   - Arquivo: `/screenshots/swagger-docs.png`
   - Executar: http://localhost:8000/api/v1/docs/

2. **Jazzmin Admin Dashboard**
   - Arquivo: `/screenshots/jazzmin-dashboard.png`
   - Executar: http://localhost:8000/admin/

3. **Insomnia API Testing**
   - Arquivo: `/screenshots/insomnia-collections.png`
   - Compartilhar coleção Insomnia

4. **Docker Containers**
   - Arquivo: `/screenshots/docker-containers.png`
   - Executar: `docker ps`
---

## 📞 Contato

Desenvolvido por [José Antonio]

- **LinkedIn:** [linkedin.com/in/jose-antonio-463281320/](https://www.linkedin.com/in/jose-antonio-463281320/)
- **GitHub:** [github.com/joseantonioalmeida](https://github.com/joseantonioalmeida)
- **Email:** joseantonioalmeida217@gmail.com

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

- Django Community
- Django REST Framework Team
- Celery & RabbitMQ
- PostgreSQL

---

**Última atualização:** Maio de 2026

⭐ Se este projeto foi útil, deixe uma estrela no GitHub! ⭐