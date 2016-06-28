var newApp = angular.module('new', []);

newApp.controller('mainCtrl', ['$scope', 'renderFactory', function ($scope, renderFactory) {
    $scope.text = 'Hello';
    console.log('in');
    init();

    function init() {
        renderFactory.createCamera();
        renderFactory.createSphere();
        renderFactory.setup();
        renderFactory.paint();
    }

}]);

newApp.factory('renderFactory', function renderFactory() {
    var xrotation;
    var yrotation;
    var zrotation;
    var WIDTH = 800;
    var HEIGHT = 600;
    var ASPECT = WIDTH / HEIGHT;
    var renderer = new THREE.WebGLRenderer();
    var scene = new THREE.Scene();
    var camera;
    var sphere;

    return {
        createSphere: function () {
            // set up the cube vars
            var length = 50;
            var segments = 16;

            // create the cube's material
            var sphereMaterial = new THREE.MeshLambertMaterial({
                color: 0xFF0000
            });

            // create a new mesh with cube geometry -
            sphere = new THREE.Mesh(new THREE.SphereGeometry( 5, 32, 32 ), sphereMaterial);

            //Set Cube Rotation
            sphere.rotation.x += 0.2;
            sphere.rotation.y += 0.3;
            sphere.rotation.z += 0.1;

            scene.add(new THREE.AmbientLight(0xFF0000));

            scene.add(sphere);

        },
        createCamera: function () {
            // set some camera attributes
            var VIEW_ANGLE = 40;
            var NEAR = 0.1;
            var FAR = 10000;

            // create a WebGL camera
            camera = new THREE.PerspectiveCamera(VIEW_ANGLE,
            ASPECT,
            NEAR,
            FAR);

            // the camera starts at 0,0,0 so pull it back
            camera.position.z = 250;

            // and the camera
            scene.add(camera);

        },
        paint: function () {
            // draw!
            renderer.render(scene, camera);
        },
        setup: function () {
            // start the renderer
            renderer.setSize(WIDTH, HEIGHT);
            document.getElementById('container1').appendChild(renderer.domElement);

        }

    };
});