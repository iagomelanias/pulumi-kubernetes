// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";

export class FirewallRule extends lumi.NamedResource implements FirewallRuleArgs {
    public readonly endIpAddress: string;
    public readonly _name: string;
    public readonly resourceGroupName: string;
    public readonly serverName: string;
    public readonly startIpAddress: string;

    constructor(name: string, args: FirewallRuleArgs) {
        super(name);
        this.endIpAddress = args.endIpAddress;
        this._name = args._name;
        this.resourceGroupName = args.resourceGroupName;
        this.serverName = args.serverName;
        this.startIpAddress = args.startIpAddress;
    }
}

export interface FirewallRuleArgs {
    readonly endIpAddress: string;
    readonly _name: string;
    readonly resourceGroupName: string;
    readonly serverName: string;
    readonly startIpAddress: string;
}
