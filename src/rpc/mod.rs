use std::collections::HashMap;

use self::config::create_config_mod;
use pyo3::prelude::*;

pub mod config;

pub fn create_rpc_mod(py: Python<'_>) -> PyResult<&PyModule> {
    let rpc_mod = PyModule::new(py, "rpc")?;
    let config_mod = create_config_mod(py)?;
    let submodules = [config_mod];
    let modules: HashMap<String, &PyModule> = submodules
        .iter()
        .map(|x| (format!("solders.rpc.{}", x.name().unwrap()), *x))
        .collect();
    let sys_modules = py.import("sys")?.getattr("modules")?;
    sys_modules.call_method1("update", (modules,))?;
    for submod in submodules {
        rpc_mod.add_submodule(submod)?;
    }
    Ok(rpc_mod)
}