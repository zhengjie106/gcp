/**
 *  * Background Cloud Function.
 *   *
 *    * @param {object} event The Cloud Functions event.
 *     * @param {function} callback The callback function.
 *      */
exports.helloBackground = function helloBackground (event, callback) {
	  callback(null, `Hello ${event.data.name || 'World'}!`);
};
