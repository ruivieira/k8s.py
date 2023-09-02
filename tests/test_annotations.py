import subprocess
import k8sutils.deployments as deployments
import k8sutils.deployments.utils as deploymentsutils


def test_get_rethrows_exception():
    # Provide an invalid namespace to induce an error
    invalid_namespace = "non_existent_namespace"

    try:
        deployments.get(namespace=invalid_namespace)
        assert False, "Expected a CalledProcessError but none was raised"
    except subprocess.CalledProcessError:
        pass  # Test passes if this exception is caught

    except Exception as e:
        assert False, f"Expected a CalledProcessError but got {type(e)}"


def test_deployment_table():
    try:
        deploymentsutils.table()
        assert False, "Expected a CalledProcessError but none was raised"
    except subprocess.CalledProcessError:
        pass  # Test passes if this exception is caught

    except Exception as e:
        assert False, f"Expected a CalledProcessError but got {type(e)}"
