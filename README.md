# Haproxy and Keepalived for Resiliancy

This sets up an haproxy instance to distribute requests to
etcd and kube-apiserver servers.  Keepalived is set up to provide
resiliancy for kube-apiserver.

Haproxy can be enabled by setting `haproxy_enabled` to `true`.  When enabled,
haproxy runs on all masters.

The haproxy stats service is started on port 2382 by default on the 127.0.0.1
interface. Set up ssh port forwarding and point your browser at it.

## etcd
Haproxy is configured to forward port 2381 (by default)
to the etcd servers running on all masters (port `haproxy_etcd_port`, which is
2379 by default). The "primary" master is given a lower priority since this
node has other traffic going to it and tends to be overloaded.

If haproxy is enabled, you'll need to configure clients to use it. For example,
to get kubeadm to use it, set the `kubernetes_master_etcd_override` to send
its requests to haproxy rather than directly to etcd by setting it to
https://127.0.0.1:2381 (the port must match `haproxy_etcd_port`).

## kube-apiserver
Haproxy will forward ports `networks.node_management.k8s_virtual_ip:6442` and
`networks.customer_management.k8s_virtual_ip:6442` to the kube-apiservers
over the node management network.  The kube-apiservers are listening at *::6443.

Keepalived is configured to manage the VIPs on the node management network and
the customer management network.

When enabled, the kubeadm configuration needs to be changed to use
`networks.node_management.k8s_virtual_ip:6442` as the `controlPlaneEndpoint`.
