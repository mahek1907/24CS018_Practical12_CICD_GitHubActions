const jwt = require("jsonwebtoken");

function auth(req, res, next) {
    const authHeader = req.headers.authorization || req.headers.Authorization;

    if (!authHeader) {
        return res.status(401).json({
            message: "Access denied. No token provided."
        });
    }

    if (!authHeader.startsWith("Bearer ")) {
        return res.status(401).json({
            message: "Access denied. Token must be in 'Bearer <token>' format."
        });
    }

    const token = authHeader.split(" ")[1];

    if (!token || token.trim() === "") {
        return res.status(401).json({
            message: "Access denied. Token is missing."
        });
    }

    try {
        const secret = process.env.JWT_SECRET || "p7_task_manager_secure_jwt_secret_key_2026_charusat";
        const decoded = jwt.verify(token, secret);
        req.user = decoded;
        next();
    } catch (error) {
        if (error.name === "TokenExpiredError") {
            return res.status(401).json({
                message: "Token expired. Please log in again."
            });
        }

        if (error.name === "JsonWebTokenError") {
            return res.status(401).json({
                message: "Invalid or tampered token."
            });
        }

        return res.status(401).json({
            message: "Authentication failed. Unauthorized access."
        });
    }
}

module.exports = auth;
