var demo = new CANNON.Demo();
var size = 3;

demo.addScene("Box", function()
{

    // Create world 
    var world = demo.getWorld();
    world.gravity.set(0,0,-10);
    world.broadphase = new CANNON.NaiveBroadphase();

    // Create a static sphere
    var sphereShape = new CANNON.Sphere(0.1),
        sphereBody = new CANNON.Body({ mass: 0 });
    sphereBody.addShape(sphereShape);
    world.add(sphereBody);
    demo.addVisual(sphereBody);

    // Create a box body
    var halfExtents = new CANNON.Vec3(size,size*0.3,size),
        boxShape = new CANNON.Box(halfExtents);
        boxBody = new CANNON.Body({ mass: 5 });
    boxBody.addShape(boxShape);
    boxBody.position.set(-size,0,-size);
    world.add(boxBody);
    demo.addVisual(boxBody);

    var spring = new CANNON.Spring(boxBody,sphereBody,{
        localAnchorA: new CANNON.Vec3(size,0,size),
        localAnchorB: new CANNON.Vec3(0,0,0),
        restLength : 0,
        stiffness : 5,
        damping : 1,
    });

    // Compute the force after each step
    world.addEventListener("postStep",function(event){
        spring.applyForce();
    });
});

demo.start();
