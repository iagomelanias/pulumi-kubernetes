// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";

export class MaintenanceWindow extends lumi.NamedResource implements MaintenanceWindowArgs {
    public readonly allowUnassociatedTargets?: boolean;
    public readonly cutoff: number;
    public readonly duration: number;
    public readonly enabled?: boolean;
    public readonly _name: string;
    public readonly schedule: string;

    constructor(name: string, args: MaintenanceWindowArgs) {
        super(name);
        this.allowUnassociatedTargets = args.allowUnassociatedTargets;
        this.cutoff = args.cutoff;
        this.duration = args.duration;
        this.enabled = args.enabled;
        this._name = args._name;
        this.schedule = args.schedule;
    }
}

export interface MaintenanceWindowArgs {
    readonly allowUnassociatedTargets?: boolean;
    readonly cutoff: number;
    readonly duration: number;
    readonly enabled?: boolean;
    readonly _name: string;
    readonly schedule: string;
}
