#!/bin/bash
uvicorn simple:app --host 0.0.0.0 --port $PORT
