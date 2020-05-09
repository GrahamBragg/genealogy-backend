import express, { Request, Response, NextFunction } from "express";
import compression from "compression";  // compresses requests
import session from "express-session";
import bodyParser from "body-parser";
import lusca from "lusca";
import mongo from "connect-mongo";
import path from "path";
import mongoose from "mongoose";
import bluebird from "bluebird";
import { MONGODB_URI, SESSION_SECRET } from "./util/secrets";
import expressStatusMon, { ExpressStatusMonitorConfig } from "express-status-monitor";

const MongoStore = mongo(session);

// Controllers (route handlers)
//import * as indexRouter from "./routes";
import indexRouter from "./routes/index";
import personRouter from "./routes/person";
import logger from "./util/logger";

// Create Express server
const app = express();

// Connect to MongoDB
const mongoUrl = MONGODB_URI;
mongoose.Promise = bluebird;

mongoose.connect(mongoUrl, { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true } ).then(
    () => { /** ready to use. The `mongoose.connect()` promise resolves to undefined. */ },
).catch(err => {
    console.log("MongoDB connection error. Please make sure MongoDB is running. " + err);
    // process.exit();
});

// Express configuration
app.set("port", process.env.PORT || 3000);
app.use(compression());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    resave: true,
    saveUninitialized: true,
    secret: SESSION_SECRET,
    store: new MongoStore({
        url: mongoUrl,
        autoReconnect: true
    })
}));
app.use(lusca.xframe("SAMEORIGIN"));
app.use(lusca.xssProtection(true));

app.use(
    express.static(path.join(__dirname, "public"), { maxAge: 31557600000 })
);

const expressConfig: ExpressStatusMonitorConfig = {
    title: "Express Status",  // Default title
    theme: "default.css",     // Default styles
    path: "/status",
    socketPath: "/socket.io"
};

app.use(expressStatusMon(expressConfig));

/**
 * Primary app routes.
 */
app.all("*", (req: Request, res: Response, next: NextFunction) => {
    logger.debug(req.method + " " + req.url);
    next();
});
app.use("/", indexRouter);
app.use("/api/v1/persons", personRouter);

export default app;
