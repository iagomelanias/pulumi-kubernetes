import pulumi
import pulumi.runtime

from ... import tables

class APIService(pulumi.CustomResource):
    """
    APIService represents a server for a particular GroupVersion. Name must be "version.group".
    """
    def __init__(self, __name__, __opts__=None, metadata=None, spec=None, status=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'apiregistration.k8s.io/v1'
        __props__['kind'] = 'APIService'
        __props__['metadata'] = metadata
        __props__['spec'] = spec
        __props__['status'] = status

        super(APIService, self).__init__(
            "kubernetes:apiregistration/v1:APIService",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
