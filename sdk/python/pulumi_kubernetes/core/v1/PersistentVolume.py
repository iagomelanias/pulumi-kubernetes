import pulumi
import pulumi.runtime

from ... import tables

class PersistentVolume(pulumi.CustomResource):
    """
    PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to
    a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes
    """
    def __init__(self, __name__, __opts__=None, metadata=None, spec=None, status=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'v1'
        __props__['kind'] = 'PersistentVolume'
        __props__['metadata'] = metadata
        __props__['spec'] = spec
        __props__['status'] = status

        super(PersistentVolume, self).__init__(
            "kubernetes:core/v1:PersistentVolume",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
