import pulumi
import pulumi.runtime

from ... import tables

class Event(pulumi.CustomResource):
    """
    Event is a report of an event somewhere in the cluster. It generally denotes some state change
    in the system.
    """
    def __init__(self, __name__, __opts__=None, action=None, deprecated_count=None, deprecated_first_timestamp=None, deprecated_last_timestamp=None, deprecated_source=None, event_time=None, metadata=None, note=None, reason=None, regarding=None, related=None, reporting_controller=None, reporting_instance=None, series=None, type=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'events.k8s.io/v1beta1'
        __props__['kind'] = 'Event'
        if not eventTime:
            raise TypeError('Missing required property eventTime')
        __props__['eventTime'] = event_time
        __props__['action'] = action
        __props__['deprecatedCount'] = deprecated_count
        __props__['deprecatedFirstTimestamp'] = deprecated_first_timestamp
        __props__['deprecatedLastTimestamp'] = deprecated_last_timestamp
        __props__['deprecatedSource'] = deprecated_source
        __props__['metadata'] = metadata
        __props__['note'] = note
        __props__['reason'] = reason
        __props__['regarding'] = regarding
        __props__['related'] = related
        __props__['reportingController'] = reporting_controller
        __props__['reportingInstance'] = reporting_instance
        __props__['series'] = series
        __props__['type'] = type

        super(Event, self).__init__(
            "kubernetes:events.k8s.io/v1beta1:Event",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
