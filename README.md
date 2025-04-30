# AI-Enhanced Real-Time Occupancy Planning System

This prototype implements a Natural Language Interface for the Occupancy Query system that integrates VergeSense sensor data with AI models to provide intelligent workspace recommendations based on natural language requests.

## Project Overview

The system allows employees to query available desks using natural language (e.g., "Find me a standing desk near the cafeteria tomorrow") and receive intelligent desk recommendations based on real-time availability, employee preferences, and organizational policies.

### Key Features

- **Natural Language Processing**: Query available desks using conversational language
- **Real-time Occupancy Integration**: Uses VergeSense API for live occupancy data
- **AI-Powered Recommendations**: Leverages OpenAI GPT and Anthropic Claude for intelligent analysis
- **Employee Preference Matching**: Considers individual preferences when making recommendations
- **Policy Compliance**: Enforces organizational workspace policies
- **RESTful API**: Clean endpoints for integration with existing systems
- **Simple Web Interface**: Demonstration UI for easy testing

## System Architecture

This system consists of these core components:

1. **FastAPI Backend**: Handles requests, integrates AI models, and processes desk recommendations
2. **AI Integration Layer**: Connects to OpenAI and Claude models for natural language understanding
3. **VergeSense Client**: Retrieves real-time occupancy data from VergeSense sensors
4. **Database Layer**: Stores desk information, employee preferences, and sensor mapping
5. **Web Frontend**: Simple interface for demonstration purposes

## Technical Implementation

### Technology Stack

- **Backend**: Python 3.8+ with FastAPI
- **Database**: SQLite (easily replaceable with PostgreSQL for production)
- **AI Models**: OpenAI GPT-4 and Anthropic Claude
- **External API**: VergeSense Occupancy API
- **Frontend**: HTML, CSS (Bootstrap), and JavaScript

### Data Models

The system uses three primary data models:

1. **Desk**: Represents physical desks with attributes like location, features, and VergeSense area mapping
2. **Employee**: Stores employee information and workspace preferences
3. **Occupancy Data**: Real-time area-level occupancy from VergeSense sensors

### Core Workflows

1. **Natural Language Query Processing**:
   - User submits a natural language query
   - AI model extracts desk requirements and preferences
   - System retrieves real-time desk availability from VergeSense
   - Matching algorithm finds suitable desks based on requirements and policies
   - Ranked recommendations are returned to the user

2. **Employee Preference Integration**:
   - System retrieves employee-specific preferences when employee ID is provided
   - Desk matching considers both explicit query requirements and stored preferences
   - Results are tailored to individual needs while maintaining policy compliance

## Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for GPT integration)
- Anthropic API key (optional, for Claude integration)
- VergeSense API credentials (the system includes mock data if unavailable)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vergesense-nlp-query.git
   cd vergesense-nlp-query
