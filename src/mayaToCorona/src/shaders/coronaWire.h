#include <maya/MPxNode.h>
#include <maya/MTypeId.h>

// Plugin CoronaWire Shader Class //

class CoronaWire : public MPxNode
{
public:
                    CoronaWire();
    virtual         ~CoronaWire();

    static  void *  creator();
    virtual MStatus compute( const MPlug&, MDataBlock& );
    static  MStatus initialize();

    virtual void    postConstructor();

    static  MTypeId   id;

protected:

};