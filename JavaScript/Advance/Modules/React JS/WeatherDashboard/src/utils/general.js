const normalizeName = (name) => {
    return name.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
};

export {normalizeName}