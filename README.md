# HemoConnect - Next-Gen Blood Donation & Emergency Matching Platform

HemoConnect is a premium, full-stack, futuristic 3D healthcare platform designed for high-speed blood matching, emergency broadcasts, and institutional coordination. It features a dark-themed glassmorphism interface, real-time radar mapping, Spring Boot controllers, Firebase Firestore integration, and built-in AI diagnostic modules.

---

## 🌟 Key Features
- **Modern 3D User Experience (Phase 2)**: Parallax tilt card micro-interactions, canvas-driven background blood cell particles, and glowing neon components.
- **Rose Four Loading State**: A custom mathematical curve loader overlaying the application during all API requests and transactions.
- **Smart Matching ABO Engine (Phase 9)**: ABO/Rh blood compatibility validations ranking candidates based on availability, proximity, and compatibility score.
- **HemoAI Insights (Phase 11)**: Integrated diagnostic checker for donor physical eligibility, emergency priority factor estimator, inventory forecast predictor, and iron-loading recovery advisor chatbot.
- **Role-Based Workflows**: Custom dashboard layouts for Donors, Recipients, Blood Banks, Hospitals, and Admins.

---

## 🔒 Security Architectures (Taha Jaffri Rules)
1. **Isolated Secrets**: Keys are externalized to environment variables and properties; no credentials exist in client source files.
2. **IP Rate Limiting**: Auth endpoints restricted to 5 requests / 15 minutes, AI logic to 10 requests / minute, and generic APIs to 60 requests / minute.
3. **MIME & Upload Filters**: Multipart file uploads verified by size constraints (<5MB) and media types on the server.
4. **Exception Shielding**: Global interceptors capture errors, log details on the server, and return generic messages to clients to prevent schema leaks.
5. **CORS Origins**: whitelisting restricted via configuration property; wildcard origins are disabled in production.

---

## 🚀 Setup & Execution

### Prerequisites
- **Java JDK 21**
- **Maven 3.9+**

### Local Run (Mock Mode / zero-config)
To run the platform out-of-the-box using the thread-safe local in-memory fallback database:
1. Clone or navigate to the project directory:
   ```bash
   cd HemoConnect
   ```
2. Launch the application:
   ```bash
   mvn spring-boot:run
   ```
3. Open your browser and navigate to `http://localhost:8080`.
4. Go to the **Settings** tab and click **Seeding Demo Data** to populate the lists instantly.

### Running with Firebase (Firestore & Authentication)
1. **Authentication**: Go to Firebase Console -> Authentication -> Sign-in Method, and enable **Email/Password** and **Phone**.
2. **Firestore**: Enable Firestore Database and create the following collections:
   - `donors`
   - `blood_requests`
   - `blood_banks`
   - `hospitals`
   - `admins`
   - `notifications`
3. **Private Key**: Switch to Project Settings -> Service accounts, and click **Generate new private key**.
4. Save the downloaded private key inside the project directory:
   `src/main/resources/serviceAccountKey.json`
5. Relaunch using:
   ```bash
   mvn spring-boot:run
   ```
   The backend will detect the file and connect to your live Firestore collections!

---

## 📡 REST API Specifications

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/donors` | Retrieves all registered donors | No |
| **POST** | `/api/donors` | Registers a new donor profile | No |
| **POST** | `/api/requests` | Creates a new blood request | User Token |
| **GET** | `/api/requests/{id}/matches` | Returns compatible donors from matching engine | User Token |
| **POST** | `/api/emergency` | Creates a critical request and triggers donor email alerts | Hospital / Admin |
| **POST** | `/api/hospitals/verify` | Validates corporate email and Hospital Access Key (HAK) | No |
| **GET** | `/api/analytics` | Compiles stats for charts and progress meters | No |
| **POST** | `/api/ai/chat` | Communicates with the AI advice chatbot | No |

---

## ☁️ Deployment Strategies

### Frontend (Firebase Hosting)
Configure Firebase CLI and deploy the static resources:
1. Log in to Firebase:
   ```bash
   firebase login
   ```
2. Initialize project:
   ```bash
   firebase init hosting
   ```
   - Select your project `hemoconnect-ak47`.
   - Set the public directory to: `src/main/resources/static`.
3. Deploy:
   ```bash
   firebase deploy --only hosting
   ```

### Backend (Google Cloud Run / Containerized)
We provide a `Dockerfile` setup to build and deploy the container to Cloud Run, which connects natively with Firebase resources:
1. Build the Maven jar:
   ```bash
   mvn clean package -DskipTests
   ```
2. Deploy the container:
   ```bash
   gcloud run deploy hemoconnect-backend --source .
   ```
