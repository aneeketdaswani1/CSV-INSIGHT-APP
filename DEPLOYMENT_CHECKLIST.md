# 🚀 Deployment Checklist

Quick reference for deploying DataSense AI to production.

## Local Testing ✅

- [ ] All dependencies installed: `pip install -r requirements.txt`
- [ ] API key configured: `echo 'ANTHROPIC_API_KEY=sk-ant-...' > .env`
- [ ] App runs locally: `streamlit run app.py`
- [ ] Sample datasets load: Click each demo button
- [ ] AI chat works: Ask Claude a question
- [ ] PDF export works: Generate and download report
- [ ] All 3 charts render: Histogram, bar chart, heatmap

## Pre-Deployment ✅

- [ ] Code committed: `git add . && git commit -m "Polish for portfolio"`
- [ ] Git pushed: `git push origin main`
- [ ] README reviewed: Clear and professional
- [ ] No API keys in code: Check with `grep -r "sk-ant-" .`
- [ ] .env in .gitignore: Should not be tracked
- [ ] Sample datasets included in repo

## Streamlit Cloud (Recommended) 🎈

```bash
# 1. Go to https://share.streamlit.io
# 2. Click "New app"
# 3. Select your GitHub repo
# 4. Select branch: main
# 5. Set main file path: app.py

# 6. After deployment, add secret:
#    Settings → Secrets
#    Add: ANTHROPIC_API_KEY = sk-ant-...
```

- [ ] Repository connected
- [ ] Branch set to main
- [ ] Main file: app.py
- [ ] ANTHROPIC_API_KEY added as secret
- [ ] App deployed and running
- [ ] Live URL working
- [ ] Sample datasets load in production

## Heroku Deployment 🐳

```bash
# 1. Install Heroku CLI
# 2. Login
heroku login

# 3. Create app
heroku create YOUR_UNIQUE_APP_NAME

# 4. Add Procfile and config.toml (already included)

# 5. Deploy
git push heroku main

# 6. Add environment variable
heroku config:set ANTHROPIC_API_KEY=sk-ant-...

# 7. Check logs
heroku logs --tail
```

- [ ] Heroku account created
- [ ] Heroku CLI installed
- [ ] App created on Heroku Dashboard
- [ ] Procfile present in repo
- [ ] Deploy with: `git push heroku main`
- [ ] API key configured: `heroku config:set ...`
- [ ] Logs checked for errors
- [ ] Live app URL verified

## Docker Deployment 🐳

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

- [ ] Docker installed
- [ ] Dockerfile created (or use above)
- [ ] Build: `docker build -t datasense-ai .`
- [ ] Run: `docker run -p 8501:8501 datasense-ai`
- [ ] Test locally at `http://localhost:8501`

## Post-Deployment ✅

- [ ] App loads without errors
- [ ] Hero header displays correctly
- [ ] Sample data buttons work
- [ ] Upload new CSV works
- [ ] AI chat functional
- [ ] PDF export works
- [ ] Share live URL with demo link

## Portfolio Sharing ✅

- [ ] GitHub repository public
- [ ] README visible on main page
- [ ] Add to portfolio with link
- [ ] Share live Streamlit Cloud link
- [ ] Screenshot app for portfolio
- [ ] Video walkthrough (optional)

## Performance Monitoring

- [ ] Monitor app speed
- [ ] Check error logs weekly
- [ ] Monitor API usage
- [ ] Track user interactions
- [ ] Update features based on feedback

---

## Quick Links

- **Streamlit Cloud**: https://share.streamlit.io
- **Heroku Dashboard**: https://dashboard.heroku.com
- **Anthropic Console**: https://console.anthropic.com
- **Repository**: https://github.com/yourusername/DataSense-AI

---

**Deployed successfully? 🎉 Share the link everywhere!**
