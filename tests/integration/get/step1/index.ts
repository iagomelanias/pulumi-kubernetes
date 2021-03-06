// Copyright 2016-2018, Pulumi Corporation.  All rights reserved.

import * as k8s from "@pulumi/kubernetes";

//
// `get`s the Kubernetes Dashboard, which is deployed by default in minikube.
//

k8s.core.v1.Service.get("kube-dashboard", "kubernetes");

//
// Create a CustomResourceDefinition, a CustomResource, and then `.get` it.
//

const ct = new k8s.apiextensions.v1beta1.CustomResourceDefinition("crontab", {
    metadata: { name: "crontabs.stable.example.com" },
    spec: {
        group: "stable.example.com",
        version: "v1",
        scope: "Namespaced",
        names: {
            plural: "crontabs",
            singular: "crontab",
            kind: "CronTab",
            shortNames: ["ct"]
        }
    }
});

new k8s.apiextensions.CustomResource(
    "my-new-cron-object",
    {
        apiVersion: "stable.example.com/v1",
        kind: "CronTab",
        metadata: { name: "my-new-cron-object" },
        spec: { cronSpec: "* * * * */5", image: "my-awesome-cron-image" }
    },
    { dependsOn: ct }
);

const ctObj = k8s.apiextensions.CustomResource.get("my-new-cron-object-get", {
    apiVersion: "stable.example.com/v1",
    kind: "CronTab",
    id: "my-new-cron-object"
});
