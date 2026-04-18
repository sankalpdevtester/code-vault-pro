# CodeVault: Developer Workspace & Portfolio Manager

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Project Status](https://img.shields.io/badge/status-Under%20Development-orange.svg)
![Frontend Stack](https://img.shields.io/badge/Frontend-React%20%7C%20Next.js%20%7C%20TypeScript%20%7C%20TailwindCSS-informational.svg)
![Backend Stack](https://img.shields.io/badge/Backend-FastAPI%20%7C%20SQLite-success.svg)

---

## Description

CodeVault is a comprehensive personal developer workspace designed to streamline the management of a developer's digital assets. It provides a centralized platform for organizing code snippets, technical notes, and project ideas. Beyond resource management, CodeVault empowers developers to curate a professional online portfolio, complete with live project showcases, making it easier to present their work to potential employers or collaborators effectively. This tool aims to be the go-to solution for developers looking to centralize their resources and enhance their professional online presence.

## Features

-   **Code Snippet Management**: Store, categorize, and search your most used or essential code snippets.
-   **Technical Note Organization**: Keep track of technical knowledge, research, and learning insights.
-   **Project Idea Incubation**: Document and develop your project concepts from ideation to planning.
-   **Professional Portfolio Builder**: Create and manage a personal developer portfolio.
-   **Live Project Showcases**: Integrate live demos or links to deployed projects directly into your portfolio.
-   **Centralized Resource Hub**: A single source of truth for all your development-related resources.
-   **Seamless Presentation**: Easily share your portfolio and work with others.
-   **User Authentication**: Secure user registration and login.
-   **Responsive UI**: Optimized for various devices and screen sizes using Tailwind CSS.

## Installation

To get CodeVault up and running on your local machine, follow these steps. Ensure you have Node.js, npm (or Yarn), Python 3.8+, and pip installed.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/codevault.git
cd codevault
```

### 2. Backend Setup (FastAPI)

Navigate to the `backend` directory, set up a virtual environment, install dependencies, and start the server.

```bash
cd backend

# Create and activate a Python virtual environment
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate

# Install backend dependencies
pip install -r requirements.txt

# Create a .env file for backend environment variables
# cp .env.example .env
# Example .env content:
# DATABASE_URL="sqlite:///./sql_app.db"
# SECRET_KEY="your-super-secret-key"
# ALGORITHM="HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES=30

# Run the FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The backend server should now be running at `http://localhost:8000`.

### 3. Frontend Setup (Next.js)

Open a **new terminal window/tab**, navigate back to the project root, install frontend dependencies, and start the development server.

```bash
cd .. # Go back to the project root

# Install frontend dependencies
npm install # or yarn install

# Create a .env.local file for frontend environment variables
# cp .env.local.example .env.local
# Example .env.local content:
# NEXT_PUBLIC_API_BASE_URL="http://localhost:8000"

# Start the Next.js development server
npm run dev # or yarn dev
```
The frontend application should now be running at `http://localhost:3000`.

## Usage

Once both the backend and frontend servers are running:

1.  Open your web browser and navigate to `http://localhost:3000`.
2.  **Sign Up**: Register for a new account using your email and password.
3.  **Log In**: Access your personal developer workspace.
4.  **Explore**:
    *   Use the navigation to manage your code snippets, technical notes, and project ideas.
    *   Visit the Portfolio section to build and customize your professional showcase.
    *   Add details for live projects, including links to deployed applications or repositories.

Start centralizing your development resources and enhance your professional online presence with CodeVault!

## Folder Structure

```
.
├── src/                      # Frontend (Next.js) application source
│   ├── components/           # Reusable UI components
│   ├── pages/                # Next.js pages/routes
│   ├── hooks/                # Custom React hooks
│   ├── lib/                  # Utility functions, API helpers, constants
│   ├── types/                # TypeScript type definitions
│   ├── styles/               # Global styles, Tailwind CSS configuration
│   └── (other Next.js specific files)
├── backend/                  # Backend (FastAPI) application source
│   ├── app/                  # Main FastAPI application
│   │   ├── api/              # API endpoints (routers)
│   │   ├── models/           # Database models (SQLAlchemy)
│   │   ├── schemas/          # Pydantic schemas for request/response validation
│   │   ├── crud/             # CRUD operations for database interaction
│   │   ├── core/             # Configuration, settings, dependencies
│   │   └── main.py           # FastAPI application entry point
│   ├── venv/                 # Python virtual environment (ignored by Git)
│   └── requirements.txt      # Backend dependencies
├── public/                   # Static assets for Next.js (images, fonts, favicon, etc.)
├── docs/                     # Project documentation, API documentation, architecture diagrams
├── config/                   # Global configuration files, environment variable templates
├── .env.example              # Example environment variables for both frontend & backend
├── package.json              # Frontend dependencies and scripts
├── tsconfig.json             # TypeScript configuration for frontend
├── next.config.js            # Next.js specific configuration
├── tailwind.config.js        # Tailwind CSS configuration
├── postcss.config.js         # PostCSS configuration for Tailwind
└── README.md                 # Project README file
```

## Contributing

We welcome contributions to CodeVault! If you'd like to contribute, please follow these steps:

1.  **Fork** the repository.
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3.  **Make your changes**, ensuring they adhere to the project's coding standards.
4.  **Commit your changes** with a clear and descriptive message: `git commit -m "feat: Add new awesome feature"`.
5.  **Push your branch** to your forked repository: `git push origin feature/your-feature-name`.
6.  **Open a Pull Request** to the main `dev` branch of the original repository, describing your changes and their benefits.

Please report any bugs or suggest features by opening an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.